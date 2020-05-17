# 项目导入到Eclipse

# 讲解

@Controller层
@RequestMapping("/users")    // users表示form传过来
```java
@Controller
@RequestMapping("/user") // 公共路径
public class NewUserCOntroller(){


    @RequestMapping("/login")
    public MOddelAndView longin(String uName, String uPwd){
        System.out.println(uName+"---->"+uPwd);
        return null;
    }
    @RequestMapping("/login2")
    public ModelAndView login2(User user, HttpServletRequest request){
        ModelAndView mav = new ModelAndView();
        Message msg = userService.login(user);
        if(msg.getMsg().equals("succeed")){
            msg.setMsg("");
            request.getSession().setAttribute("msgl", msg);
            mav.setViewName("redirect:/index.jsp");
            return mav
        }
        else{
            mav.addObject("msgl",msg);
            mav.setViewName("redirect:/login.jsp);
        }
    }
}

```
```html
iframe 
```

## jquery $("#iframe")

## sql 的模糊匹配
## ajax 请求
```ajax
$.ajax({
    type:"post",
    url:"kinds/addKind",
    data:$("#form").serialize(),
    dataType:'json',
    async:true,
    success:function(data){
        if(data.msg == "success"){
            func();
            ......
        }
        else{
            ......
        }
    }
})
```

## foreach 
varStatus = "stat"
## @ResponseBody