//动态添加消息
function AddMessageBox(){
    var data = arguments[0] ? arguments[0] : "";
    var color = arguments[1] ? arguments[1] : "white";
    $("#main").append("<br/><div class=\"message_box\" style=\"color:" + color + "\">" + data + "</div>");
}

//动态添加消息
function AddTickerMessageBox(){
    var data = arguments[0] ? arguments[0] : "";
    var color = arguments[1] ? arguments[1] : "white";
    $("#main").append("<br/><div class=\"message_box\" id=\"ticker\" style=\"color:" + color + "\">" + data + "</div>");
}

//动态添加命令输入部分
function AddCommandBox(){
    if (undefined != $.LS.get("user")){
        user_name = $.LS.get("user_name");
    } else {
//        user_name = "GUEST:";
        user_name = "lin@lin-SUTACM:~$";
    }
    
    $("#main").append("<br/><div class=\"command_box\"><div class=\"user_name\"><a>" + user_name + "</a></div><div class=\"command_area\"><input type=\"text\" name=\"command\"></div></div>");
}

function AddCommandBox(){
    if (undefined != $.LS.get("user")){
        user_name = $.LS.get("user_name");
    } else {
//        user_name = "GUEST:";
        user_name = "lin@lin-SUTACM:~$";
    }
    
    $("#main").append("<br/><div class=\"command_box\"><div class=\"user_name\"><a>" + user_name + "</a></div><div class=\"command_area\"><input type=\"text\" name=\"command\"></div></div>");
}

//处理写命令
function ShellCommand(command){
    var shellcommand = new Array();
    shellcommand = command.split(":");
    switch (shellcommand[0]){
        //VirtualShell命令集
        case "$vs":
            switch (shellcommand[1]){
                //清除屏幕
                case "clean":
                    $("#main").empty();
                    AddCommandBox();
                    break;              
                
                //关闭VirtualShell
                case "bye":
                    AddMessageBox("Virtual Shell will shutdown in 5 seconds", "red");
                    AddMessageBox("Good Bye!");
                    AddMessageBox("Press Ctrl+C to cancel");
                    shutdown = 5;
                    
                    shutdowntimer = setInterval(function(){
                        if ($("input:last").val() != command){
                            AddMessageBox("Virtual Shell shutdown process canceled");
                            clearInterval(shutdowntimer);
                        }
                        
                        if (shutdown){
                            shutdown--;                            
                        } else {
                            AddMessageBox("GoodBye");
                            window.opener=null;window.open('','_self', '');window.close();
                        }
                    }, 1000);
                    break;
                
                //访问github主页
                case "github":
                    window.open("https://github.com/bricksfx/gd_virtual_shell");
                    AddCommandBox();
                    break;
                    
                //显示VirtualShell指令集
                case "help":
                    AddCommandBox();
                    break;
                    
                //显示作者信息
                case "author":
                    
                    AddCommandBox();
                    break;
                    
                //用户登录
                case "login":
                    $("#main").empty();
                    if (undefined != $.LS.get("user_name")){
                        
                    }
                    
                    break;
            }
            break;
    }
}

