```c++
# include <opencv2/opencv.hpp>
# include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
	Mat src = imread("E:/Data_Media/Data_Picture/seedPictures/IMG_1303.JPG");
	if (src.empty()) {
		printf("could not load image...\n");
		getchar();
		return -1;
	}

	namedWindow("input image", WINDOW_AUTOSIZE);
	imshow("input image", src);

	//  gray 背景纯色化
	Mat gray, binary, shifted;
	// 纯化 噪点，基于金字塔的meanShift，迭代收敛的方法边缘保留，一个空间，一个color距离 ，差异小的和差异大的差距
	pyrMeanShiftFiltering(src, shifted, 21, 51);    
	// imshow("shifted", shifted);

	// binary
	cvtColor(shifted, gray, COLOR_BGR2GRAY);    // 变换成bgr2gray
	threshold(gray, binary, 0, 255, THRESH_BINARY | THRESH_OTSU);    // 二值化
	// imshow("binary", binary);

	// distance tranform
	Mat dist;
	distanceTransform(binary, dist, DistanceTypes::DIST_L2, 3, CV_32F);  // L2 是两点之间的距离
	normalize(dist, dist, 0, 1, NORM_MINMAX); // 变换之后值比较小
	// imshow("distance tranform", dist);

	// binary
	threshold(dist, dist, 0.4, 1, THRESH_BINARY);
	// imshow("distance tranform", dist);
	// 之前的没有问题

	
	// markers
	Mat dist_m;
	dist.convertTo(dist_m, CV_8U); // 变成8通道的
	vector<vector<Point>> contours(11111);
	// findContours(dist_m, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, Point(0, 0));
	findContours(dist_m, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, Point(0, 0));


	// create markers
	Mat markers = Mat::zeros(src.size(), CV_32SC1);
	for (size_t t = 0; t < contours.size(); t++){
		drawContours(markers, contours, static_cast<int>(t), Scalar::all(static_cast<int>(t)+1), -1);
	}
	circle(markers, Point(5, 5), 3, Scalar(255), -1);
	// imshow("markers", markers);

	// 形态学操作，彩色图像，目的试试去掉干扰，让结果更好
	Mat k = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));
	morphologyEx(src, src, MORPH_ERODE, k);
	 

	//完成分水岭变换
	watershed(src, markers);
	Mat mark = Mat::zeros(markers.size(), CV_8UC1);
	markers.convertTo(mark, CV_8UC1);
	bitwise_not(mark, mark, Mat());
	// imshow("watersehd", mark);
	

	// generate random color （原始白色分割）
	vector<Vec3b> colors;
	for (size_t i = 0; i < contours.size(); i++){
		int r = theRNG().uniform(0, 255);
		int g = theRNG().uniform(0, 255);
		int b = theRNG().uniform(0, 255);
		colors.push_back(Vec3b((uchar)b, (uchar)g, (uchar)r));
	}

	// 颜色填充与最终显示
	Mat dst = Mat::zeros(markers.size(), CV_8UC3);
	int index = 0;
	for (int row=0; row < markers.rows; row++){
		for (int col = 0; col < markers.cols; col++) {
			index = markers.at<int>(row, col);
			if (index > 0 && index <= contours.size()) {
				dst.at<Vec3b>(row, col) = colors[index - 1];
			}
			else{
				dst.at<Vec3b>(row, col) = Vec3b(0, 0, 0);
			}
		}
	}
	imshow("final Result", dst);
	printf("number of objects :%d", contours.size());

	waitKey(0);
	return 0;
}
```