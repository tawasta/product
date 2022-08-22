odoo.define("widget_on_hand_color", function (require) {
    "use strict";

    var FormRenderer = require("web.FormRenderer");

    FormRenderer.include({
        _renderStatButton: function (node) {
            var $button = this._super(node);
            if (
                $button.hasOwnProperty("0") &&
                $button[0].name === "action_open_quants" &&
                this.state.data.has_stock_on_several_locations === true
            ) {
                $button[0].style = "color: brown";
            }
            return $button;
        },
    });
});
