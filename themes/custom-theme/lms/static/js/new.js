alert("new js");
    var x=$(".vert.vert-${idx}").children();
    var y=x.attr("data-block-type");
    if(y=="html")
    {
      y="Course Materials";
    }
    if(y=="video")
    {
      $("#nav-${idx}").hide();
      $(".vert.vert-${idx}").css("order","-1");
    }
    y=y.charAt(0).toUpperCase() + y.slice(1);
    if(y=="Discussion")
    {
    	$("#T-${idx}").append("<p class=\"Discussion\">"+y+"</p>");
      txt="T-${idx}";
    }
    if(y=="Course Materials")
    {
    	$("#T-${idx}").append("<p class=\"Course Materials\">"+y+"</p>");
    }
  

if(!$("iframe").length)
  {
    var ele=$(".vert.vert-${idx}");  
    var a=ele.children();
    var b=a.attr("data-block-type");
    if(b=="video")
    {
      $(".vert-mod").append(ele);
    }
  }
  else
  {
    var x=$("iframe").attr("src");
    var m=$("iframe");
    m.css("width","70vw");
    m.css("height","40vw");
        var i=m.parent();
        var j=i.parent();
        var k=j.parent();
        j.has('p').css("display","none !important");
        var aa=k.attr("class");
        var num=aa.substr(10,11);
        num="#nav-"+num;
        $(num).hide();
        $(".vert-mod").prepend(k);
        k.css("padding-left","14%");
        k.css("padding-right","1.5%");
        k.css("padding-top","1%");
        k.css("padding-bottom","0%");
        k.css("margin-bottom","0 !important");
        k.css("box-shadow","0 2px 5px gray");
        m.css("border","1px solid gray");
       // $("#nav-${idx}").hide();
  }
    $("#tab-0").attr('class',"container tab-pane fade active show");