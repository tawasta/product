/** @odoo-module **/
import {SaleOrderLineProductField} from "@sale/js/sale_product_field";
import {patch} from "@web/core/utils/patch";

patch(SaleOrderLineProductField.prototype, {
    getDomain() {
        const res = super.getDomain(...arguments);
        const listen_class = document.querySelectorAll(".listen_product");
        const last_input = listen_class[listen_class.length - 1];

        if (last_input) {
            const input = last_input.getElementsByTagName("input")[0];

            if (input) {
                const written_search_term = input.value;
                const tr_element = input.closest("tr");
                const version_class = tr_element.querySelectorAll(".version_class")[0];
                const version_code_info_textarea =
                    version_class.getElementsByTagName("textarea")[0];
                version_code_info_textarea.value = written_search_term;
            }
        }
        return res;
    },
});
