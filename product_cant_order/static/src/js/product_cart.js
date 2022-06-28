odoo.define("product_cant_order.product", function () {
    "use strict";

    $("input[type=hidden][class='product_id']").bind("change", function () {
        var product_id = $(this).val();
        if (product_id) {
            var action = "/check/product/" + product_id;
            $.post(action, function (res) {
                var results = JSON.parse(res);
                if (results.error) {
                    console.error(results.error);
                } else if (results.order_status === true) {
                    $("#add_to_cart").removeClass().addClass("d-none");
                } else {
                    $("#add_to_cart")
                        .removeClass()
                        .addClass(
                            "btn btn-primary btn-lg mt16 js_check_product a-submit d-block d-sm-inline-block"
                        );
                }
                $.unblockUI();
            });
        }
    });
});
