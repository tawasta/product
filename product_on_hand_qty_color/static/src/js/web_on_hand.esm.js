/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useEffect } from "@odoo/owl";
import { FormRenderer } from "@web/views/form/form_renderer";

patch(FormRenderer.prototype, {
    setup() {
        super.setup();
        useEffect(() => this._updateButtonStyle(), () => [this.props.record]);
    },

    _updateButtonStyle() {
        setTimeout(() => {
            // Etsitään kaikki painikkeet, joilla on `name="action_update_quantity_on_hand"`
            const buttons = document.querySelectorAll("button[name='action_update_quantity_on_hand']");
            buttons.forEach((button) => {
                if (this.props.record.data.has_stock_on_several_locations) {
                    button.style.backgroundColor = "rgba(165, 42, 42, 0.2)";  // Ruskea tausta, 20% opacity
                    button.style.border = "1px solid rgba(165, 42, 42, 0.5)"; // Kevyt reuna
                }
            });
        }, 500);
    },
});
