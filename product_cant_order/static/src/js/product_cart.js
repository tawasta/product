odoo.define('product_cant_order.product', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    function checkProductAvailability(productId, callback) {
        var action = "/check/product/" + productId;
        ajax.jsonRpc(action, 'call', {product_id: productId})
            .then(function (results) {
                if (results.error) {
                    console.error(results.error);
                    callback(false);
                } else {
                    callback(results.order_status === true);
                    if (results.order_status === true) {
                        $("#add_to_cart").removeClass().addClass("d-none");
                    } else {
                        $("#add_to_cart")
                            .removeClass()
                            .addClass(
                                "btn btn-primary btn-lg mt16 js_check_product a-submit d-block d-sm-inline-block"
                            );
                    }
                }
            });
    }

    return {
        checkProductAvailability: checkProductAvailability,
    };
});
