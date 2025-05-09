/** @odoo-module **/

import {FormRenderer} from "@web/views/form/form_renderer";
import {patch} from "@web/core/utils/patch";
import {useEffect} from "@odoo/owl";

patch(FormRenderer.prototype, {
    setup() {
        super.setup();
        useEffect(
            () => this._updateButtonStyle(),
            () => [this.props.record]
        );
    },

    _updateButtonStyle() {
        setTimeout(() => {
            // Haetaan vain painikkeet, joilla on "on_hand_button"-class ja oikea name
            const buttons = document.querySelectorAll(
                "button.on_hand_button[name='action_update_quantity_on_hand']"
            );
            buttons.forEach((button) => {
                if (this.props.record.data.has_stock_on_several_locations) {
                    // Ruskea tausta, 14% opacity
                    button.style.backgroundColor = "rgba(165, 42, 42, 0.14)";
                    // Kevyt reuna
                    button.style.border = "1px solid rgba(165, 42, 42, 0.5)";
                }
            });
        }, 500);
    },
});
