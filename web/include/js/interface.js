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
            ShellCommand($("input:last").val());            
            $("input:last").focus();
            //逻辑运算
        }
        
        if (e.ctrlKey && e.which == 67){
            $("input").attr("disabled", "disabled");
            AddCommandBox();
            $("input:last").focus();
        }
    })
 })