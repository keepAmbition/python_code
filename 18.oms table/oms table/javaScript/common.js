/**
 * Created by dell on 2018/1/22.
 */
$(function () {
    $(".header").click(function () {
        var item_list = $(this).parent().siblings();
        $(this).next().removeClass("hide");
        for (var i = 0; i < item_list.length; i++) {
            $(this).parent().siblings().children("div:last-child").addClass("hide");
//          dom实现方式
//          var current_item = item_list[i];
//          current_item.children[1].classList.add("hide");

        }
    });
});

$(".all").click(function () {
    $(":checkbox").prop('checked', true);
});


$(".cancel").click(function () {
    $(":checkbox").prop('checked', false);
});

$(".reverse").click(function () {
    var a = $(":checkbox");
    for (var i = 0; i < a.length; i++) {
        console.log($(this));
        if ($(a[i]).prop("checked")) {
            $(a[i]).prop("checked", false)
        } else {
            $(a[i]).prop("checked", true)
        }
    }
});

$(".edit").click(function () {
    var list_text = $("td[class='table_text']");
    list_text.each(function () {
        //console.log(this);
        var att = $(this).attr('target');
        if ($(this).next().children().attr('name') == att) {
            var text = $(this).text();
            $(this).next().children().val(text);
        }
        if ($(this).prev().children().prop("checked")) {
            $(this).parent().children(":even").removeClass("hide");
            $(this).parent().children(":odd").addClass("hide")
        }
    });
});

$(".cancel_edit").click(function () {
    $(".table_text").removeClass("hide");
    $(".table_next").addClass("hide")
});

$(function () {
    $(":checkbox").click(function () {
        $(this).parent().siblings(".table_text").removeClass("hide").siblings(".table_next").addClass("hide");
        //不写在一行的方式
        //$(this).parent().siblings(".table_next").addClass("hide")
    })
});
$(function () {
    $(".table_text").mouseover(function () {
        $(this).css("background", "#e54346")
    })
    ;
});
$(function () {
    $(".table_text").mouseout(function () {
        $(".table_text").css("background", "")
    });
});
