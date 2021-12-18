function dark_mode(){
    const light = ["Background3", "Background2_1", "Project_Idea_Part", 
        "Main_Part_Text", "Box1_1", "MT1"];
    const dark = ["bg3_dark", "bg21_dark", "pip_dark","mpt_dark", "box11_dark", "MT1_dark"];
    for (var count = 0; count <dark.length; count++){
        var bg = document.getElementsByClassName(light[count]);
        for(var i = bg.length - 1; i>=0; i=i-1)
        {
            bg[i].className= dark[count];
        }
    }
}
function light_mode(){
    const light = ["Background3", "Background2_1", "Project_Idea_Part", 
        "Main_Part_Text", "Box1_1", "MT1"];
    const dark = ["bg3_dark", "bg21_dark", "pip_dark","mpt_dark", "box11_dark", "MT1_dark"];
    for (var count = 0; count <dark.length; count++){
        var bg = document.getElementsByClassName(dark[count]);
        for(var i = bg.length - 1; i>=0; i=i-1)
        {
            bg[i].className= light[count];
        }
    }
}

