// #2c3238 dark bg, #ffffff dark title text, #9aa6b3 dark content text
const light = ["MT4", "MT3", "MT2", "MT1","TnT", "Main_Part_Text2_1", "Main_Part_Text2",
        "Project_Text2", "Main_Part_Text", "Project_Text", "Project_Idea_Part2", "HardwareText2",
        "HardwareText", "Project_Des", "Project_Content", "Text1", "Header1","Project_Idea_Part","ToolandTech", 
        "body_bg", "Box1_2", "Box1_1", "logo_light"];
    const dark = ["MT4dark", "MT3dark", "MT2dark","MT1dark", "TnTdark", "Main_Part_Text2_1dark", "Main_Part_Text2dark",
        "Project_Text2dark", "Main_Part_Textdark", "Project_Textdark", "Project_Idea_Part2dark", "HardwareText2dark",
        "HardwareTextdark", "Project_Desdark", "Project_Contentdark", "Text1dark", "Header1dark", "Project_Idea_Partdark",
    "ToolandTechdark", "body_bgdark", "Box1_2dark", "Box1_1dark", "logo_dark"];
function dark_mode(){
    for (var count = 0; count <dark.length; count++){
        var bg = document.getElementsByClassName(light[count]);
        for(var i = bg.length - 1; i>=0; i=i-1)
        {
            bg[i].className= dark[count];
        }
    }
}
function light_mode(){
    for (var count = 0; count <dark.length; count++){
        var bg = document.getElementsByClassName(dark[count]);
        for(var i = bg.length - 1; i>=0; i=i-1)
        {
            bg[i].className= light[count];
        }
    }
}

function toggled(){
    if(document.getElementById("togBtn").checked == true){ //checked -> in dark mode
        dark_mode();
    } else { //unchecked -> in light mode
        light_mode();
    }
}