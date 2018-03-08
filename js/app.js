  var editor = ace.edit("editor");
  editor.setTheme("ace/theme/monokai");
    $(document).ready(function(){
      var val = $("select").val();
      editor.getSession().setMode("ace/mode/"+val);
    });

    $("select").change(function(){
      if (confirm("If you change the language all the code will be deleted. Do you want to continue?")) {
        var val = $("select").val();
        editor.getSession().setMode("ace/mode/"+val);

        if (val == "java") {
          editor.setValue('import java.util.*;\nimport java.io.*;\nimport java.math.*;\n\npublic class gamify{\n//Dont change the name of the class\n  public static void main(String []args){\n\n }\n}');
        }else {
          editor.setValue('');
        }
      }
    });


    $("#submit").click(function () {
      var data = {
        code: editor.getValue(),
        language: $(".lang").val(),
        input: $("#custinp").val()
      }
      $(".output").css("display", "none");
      $("#wish").css("display", "none");
      $("#loaderContainer").css("display", "block");
      $.ajax ({
        method: "post",
        data: "data=" + JSON.stringify(data),
        url: "phpfunctions/sendtoserver.php",
        success: function (res) {
          $("#output").html(res.replace(/\n/g,'<br/>').replace("File \"/var/www/html/GamifyString/code/gamify.py\", line", "Line").replace("/var/www/html/GamifyString/code/gamify.java", "Line ").replace("/var/www/html/GamifyString/code/gamify.cpp:", "Line "));
          setTimeout(function (){
            $("#loaderContainer").css("display", "none");
            $(".output").css("display", "block");
          }, 2000);
        },
        error: function () {
          console.log("Some error Occoured");
        },
      });

    });
