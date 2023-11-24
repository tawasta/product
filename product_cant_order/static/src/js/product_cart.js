odoo.define("product_cant_order.product", function (require) {
    "use strict";

    var ajax = require("web.ajax");

    function checkProductAvailability(productId, callback) {
        var action = "/check/product/" + productId;
        ajax.jsonRpc(action, "call", {product_id: productId}).then(function (results) {
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

    function runCheck() {
        if ($(".oe_website_sale").length && $("#add_to_cart").length) {
            var productId = $(".product_id").val();
            if (productId) {
                // eslint-disable-next-line no-unused-vars
                checkProductAvailability(productId, function (isAvailable) {
                    // Tässä voi toteuttaa lisätoimintoja riippuen isAvailable-arvosta
                });
            }
        }
    }

    $(document).ready(runCheck);

    // Tapahtumankäsittelijä .product_id kentälle
    $(".product_id").on("change", function () {
        runCheck();
    });

    // Oletusarvoinen paikka, jossa .product_id kentän arvoa muutetaan ohjelmallisesti
    // Tämän koodin sijainti riippuu siitä, missä ja milloin arvoa tarvitsee muuttaa
    function updateProductIdAndTriggerChange(newProductId) {
        $(".product_id").val(newProductId).trigger("change");
    }

    return {
        checkProductAvailability: checkProductAvailability,
        updateProductIdAndTriggerChange: updateProductIdAndTriggerChange,
    };
});
