$(function () {

    //添加操作
    $('#add_host').click(function () {
        $('.shade,.add-modal').removeClass('hide');
    });

    $('#cancel').click(function () {
        $('.shade,.add-modal').addClass('hide');
    });

    $('#ajax_submit').click(function () {
        $.ajax({
            url: "/app/test_ajax",   //url定义ajax发送请求的URL
            type: 'POST',             //type定义ajax发送请求的方法类型
            // data中则是ajax准备发送服务端的数据
            //data: {'hostname': $('#host').val(), 'ip': $('#ip').val(), 'port': $('#port').val(), 'b_id': $('#sel').val()},
            data: $('#add_form').serialize(), // 将整个form表单中的参数以字典形式发送给服务端，相比上面的写法，更加便捷
            success: function (data) {      // 服务端返回数据成功后执行的方法
                var obj = JSON.parse(data);
                if (obj.status) {
                    location.reload();       //重新加载当前页面（get形式）
                } else {
                    $('#erro_msg').text(obj.error);
                }
            }
        })
    });

    //编辑操作
    $('.edit').click(function () {
        $('.shade,.edit-modal').removeClass('hide');
        var bid = $(this).parent().parent().attr('b_id');
        var nid = $(this).parent().parent().attr('h_id');
        var n = $(this).parent().siblings().eq(1).text();
        var ip   = $(this).parent().siblings().eq(2).text();
        var port = $(this).parent().siblings().eq(3).text();
        $('#edit_form').find("input[name='hostname']").val(n);
        $('#edit_form').find('input[name="ip"]').val(ip);
        $('#edit_form').find('input[name="port"]').val(port);
        $('#edit_form').find('select').val(bid);
        $('#edit_form').find('input[name="nid"]').val(nid);

        $("#ajax_submit_edit").click(function () {
            $.ajax({
                url: "/app/edit",
                type: "POST",
                data: $('#edit_form').serialize(),
                success: function (data) {
                    var obj = JSON.parse(data);
                    if (obj.status) {
                        $('.shade,.add-modal,.edit-modal').addClass('hide');
                        location.reload();
                    } else {
                        $('#erro_msg').text(obj.error);
                    }
                }
            });

        });
        $("#cancel_submit_edit").click(function () {
            $('.shade,.edit-modal').addClass('hide');
        });
    });
    //删除操作
    $('.delete').click(function () {
    var nid = $(this).parent().parent().attr('h_id');
    $.ajax({
        url: "/app/del",
        type: "POST",
        data: {"nid": nid},
        success: function (data) {
            var obj = JSON.parse(data);
            if (obj.status) {
                location.reload();
            }
        }
    });
});
});




