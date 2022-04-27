odoo.define('widget_on_hand_color', function (require) {
    "use strict";

var FormRenderer = require('web.FormRenderer');

FormRenderer.include({
    _renderButtonBox: function (node) {
        var $button = this._super.apply(this, arguments);
        var length = node.children.length;
        var child;
        for (child = 0; child < length; child++) {
            if (typeof $button[0].children !== "undefined" &&
                    typeof $button[0].children[child] !== "undefined" &&
                    $button[0].children[child].name === "action_open_quants" &&
                    this.state.data.has_stock_on_several_locations === true) {
                $button[0].children[child].style.color = "brown";
            }
        }
        return $button;
    }
});

});
