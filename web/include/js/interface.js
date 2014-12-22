//初始界面
$(function(){
    AddMessageBox("Welcome to use the virtual shell");
    AddMessageBox("(C) SUT-ACM 2014-2015 *Chen & Bricks");
    AddMessageBox("USE $vs:help to get more information");
    AddCommandBox();
    $("input:last").focus();
})


//设定快捷键
$(function(){
    $(this).keydown(function(e){
        $("input:last").focus();        
        if (e.which == 13){
            $("input").attr("disabled", "disabled");
            //记录命令历史
            if (logined){
                if (undefined != $.LS.get("command_stack")){
                    now_command = command_array.length;
                }
                if (now_command != -1){      
                    command_array.push($("input:last").val());
                    now_command++;
                } else {
                    now_command++;                    
                    command_array[now_command] = $("input:last").val();
                }
                
                $.LS.set("command_stack", JSON.stringify(command_array));
            }
            ShellCommand($("input:last").val());            
            $("input:last").focus();
            //逻辑运算
        }
        
        if (e.ctrlKey && e.which == 67){
            $("input").attr("disabled", "disabled");
            AddCommandBox();
            $("input:last").focus();
        }
        
        if ((e.which == 38 || e.which == 40) && logined){
            CommandHistory(e.which);
        }
        
    })
 })