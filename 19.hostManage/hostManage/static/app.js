$(function () {
    //打开/关闭模态对话框操作
    $('#add_app').click(function () {
        $('.shade,.add-modal').removeClass('hide');
    });

    $('#cancel').click(function () {
        $('.shade,.add-modal').addClass('hide');
    });
    //添加操作
    $('#add_submit_ajax').click(function () {
        $.ajax({
            url: '/app/ajax_add_app',
            // data: {'user': 123,'host_list': [1,2,3,4]},
            data: $('#add_form').serialize(),
            type: "POST",
            dataType: 'JSON',   //dataType定义为JSON后，就不用再对服务端返回的数据进行反序列化
            traditional: true,  // traditional定义true后，才能支持data列表形式的value请求参数: {''host_list': [1,2,3,4]}
            success: function (obj) {
                if (obj.status) {
                    $('.shade,.add-modal').addClass('hide');
                    location.reload();
                }
            },
            error: function () {

            }

        })
    });
    //编辑操作
    $('.edit').click(function () {

        $('.edit-modal,.shade').removeClass('hide');

        var hid_list = [];
        $(this).parent().prev().children().each(function () {
            var hid = $(this).attr('hid');
            hid_list.push(hid)
        });
        $('#edit_form').find('select').val(hid_list);
        var aid = $(this).parent().siblings(":first").text();
        $('#edit_form').find('input[name="app"]').val(aid);

        var nid = $(this).parent().parent().attr("aid");
        console.log(nid);
        $('#edit_form').find('input[name="nid"]').val(nid);

        $("#ajax_submit_edit").click(function () {
            $.ajax({
                url: "/app/ajax_submit_edit",
                type: "POST",
                data: $("#edit_form").serialize(),
                dataType: "JSON",
                success: function (data) {
                    if (data.status) {
                        $('.shade,.edit-modal').addClass('hide');
                        location.reload();
                    }
                }
            })
        });

        $("#cancel_submit_edit").click(function(){
            $('.shade,.edit-modal').addClass('hide');
        });

    });
    //删除操作
    $('.delete').click(function () {
        var hid_list = [];
        $(this).parent().prev().children().each(function () {
            var hid = $(this).attr('hid');
            hid_list.push(hid)
        });
        console.log(hid_list);
        var nid = $(this).parent().parent().attr("aid");
        console.log(nid);
        $.ajax({
            url: "/app/ajax_submit_delete",
            type: "POST",
            data: {"nid": nid, "host_id_list": hid_list},
            dataType: "JSON",
            traditional: true,
            success: function (data) {
                if (data.status) {
                    location.reload();
                }
            }
        });

    });
    //查看主机信息
    $('.host-tag').click(function () {
        var nid = $(this).attr("hid");
        var aid = $(this).parent().parent().attr("aid");
        console.log(nid,aid);
        window.location.href="/app/host_detail?nid=" + nid + "&aid=" + aid;
    });
});
