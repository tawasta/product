/** @odoo-module **/
import {registry} from "@web/core/registry";
//import { SolProductMany2One } from "@sale/views/sale_order_line/sol_product_many2one";
import {SaleOrderLineProductField} from "@sale/js/sale_product_field";
import {useOpenMany2XRecord} from "@web/views/fields/relational_utils";

import {Many2OneField} from "@web/views/fields/many2one/many2one_field";
import {patch} from "@web/core/utils/patch";
// Käytä Many2one kenttää
import {useState} from "@odoo/owl";
//import { Component, useState } from "@odoo/owl";

console.log("JS file is being loaded");

//export class MyField extends Many2OneField {
//    get Many2XAutocompleteProps() {
//        const props = super.Many2XAutocompleteProps;
//        console.log("Default Many2XAutocompleteProps:", props);
//        return props
//    }
//}

//useOpenMany2XRecord({
//    resModel,
//    onRecordSaved,
//    onRecordDiscarded,
//    fieldString,
//    activeActions,
//    isToMany,
//    onClose = (isNew) => {},
//}) {
//    const res = super.useOpenMany2XRecord(...arguments);
//    console.log("useOpenMany2XRecord on SO line:", res);
//    return res;
//},

patch(SaleOrderLineProductField.prototype, {
    get Many2XAutocompleteProps() {
        const props = super.Many2XAutocompleteProps;
        //const props = super.Many2XAutocompleteProps(...arguments);
        console.log("Many2XAutocompleteProps on SO line:", props);
        //const focus = this.autocompleteContainerRef.el.querySelector("input").focus();
        //console.log("FOCUS", focus);
        //const input = self?.autocomplete?.inputEl;
        //const input = self.autocomplete;
        const input = self;
        console.log("INPUT AUTOCOMPLETE", input);
        //console.log("INPUT", input);

        return props;
    },

    //get value() {
    //    const res = super.value;
    //    console.log("GET VALUE", res);
    //    return res;
    //},

    getDomain() {
        const res = super.getDomain(...arguments);
        console.log("GET DOMAIN", res);

        //const input = document.querySelector('input[name="product_template_id"]');
        const input = document
            .querySelector(".listen_product")
            .getElementsByTagName("input")[0];
        console.log("GET INPUT", input);
        //const input = document.querySelector('input[name="product_id"]');
        // vaihtoehtoisesti: document.getElementById("product_id")

        //if (input) {
        //    input.addEventListener("input", () => {
        //        const value = input.value || "";
        //        console.log("product_id muuttui:", value);

        //        // Tässä kohtaa voit tehdä mitä haluat arvolla:
        //        writeSearchTerm("product_id", value);
        //    });
        //}

        return res;
    },

    get string() {
        const res = super.string;
        console.log("GET STRING", res);
        return res;
    },

    get displayName() {
        const res = super.displayName;
        console.log("GET DISPLAYNAME", res);
        return res;
    },

    async openDialog(resId) {
        const res = super.openDialog(...arguments);
        console.log("OPENDIALOG", res);
        return res;
    },

    setup() {
        const res = super.setup(...arguments);
        console.log("SETUP", res);
        return res;
    },

    async _onProductTemplateUpdate() {
        super._onProductTemplateUpdate(...arguments);
        console.log("ON UPDATE");
    },

    //async openMany2X() {
    //    const res = super.openMany2X(...arguments);
    //    console.log("OPEN openMany2X");
    //    return res;
    //},

    async search(barcode) {
        const res = super.search(...arguments);
        console.log("SEARCH RESULT");
        return res;
    },

    //get productName() {
    //    //const res = super.productName(...arguments);
    //    const res = super.productName;
    //    //const res = super.productName(...arguments);
    //    console.log("PRODUCT NAME");
    //    console.log(res);
    //    return res;
    //},

    mounted() {
        super.mounted?.();
        console.log("mounted");

        const input = this.el.querySelector("input");
        if (input && !input._listenerAttached) {
            console.log("Input found inside sol_product_many2one");
            input.addEventListener("input", () => {
                console.log("User typed:", input.value);
            });
            input._listenerAttached = true;
        }
    },
});

document.addEventListener("input", (ev) => {
    const target = ev.target;
    if (
        target.tagName === "INPUT" &&
        target.closest(".o_field_many2one")?.dataset.name === "product_template_id"
    ) {
        if (!handledInputs.has(target)) {
            console.log("First input in product_template_id:", target.value);
            handledInputs.add(target);
        }
    }
});

//patch(SaleOrderLineProductField.prototype, {
patch(Many2OneField.prototype, {
    //get Many2XAutocompleteProps() {
    //    const props = super.Many2XAutocompleteProps;
    //    console.log("Default Many2XAutocompleteProps:", props);
    //    return props
    //},

    //function attachInputListener(self) {
    //attachInputListener(self) {
    //    // Liitetään input-kuuntelija kerran
    //    //const input = <otetaan tarvittava kentta>
    //    const input = self?.autocomplete?.inputEl;
    //    console.log("INPUT TEST");
    //    console.log(input);
    //    //if (input) {
    //    //    input.addEventListener("input", () => {
    //    //        <tallennetaan arvo omaan kenttaan>
    //    //    });
    //    //}
    //},
    //

    mounted() {
        super.mounted(...arguments);
        if (this.props.name === "product_template_id") {
            const observer = new MutationObserver(() => {
                const input = this.el.querySelector("input");
                if (input && !input._listenerAttached) {
                    console.log("Input detected via MutationObserver");
                    input.addEventListener("input", () => {
                        console.log("User typed:", input.value);
                    });
                    input._listenerAttached = true;
                }
            });
            observer.observe(this.el, {childList: true, subtree: true});
        }
    },

    //async openAutocomplete() {
    //    const res = await super.openAutocomplete(...arguments);

    //    //if (this.props.name === "product_id") {
    //    const input = this?.autocomplete?.inputEl;
    //    if (input && !input._firstInputAttached) {
    //        console.log("product_id input field detected");

    //        input.addEventListener("input", () => {
    //            if (!input._firstValueCaptured) {
    //                console.log("First input typed:", input.value);
    //                // Optionally save to a hidden field:
    //                // this.props.record.update({ product_search_term: input.value });

    //                input._firstValueCaptured = true;
    //            }
    //        });

    //        input._firstInputAttached = true;
    //    }
    //    //}

    //    return res;
    //},

    //async openAutocomplete() {
    //    const res = await this._super(...arguments);

    //    console.log("THIS PROPS NAME");
    //    console.log(this.props.name);
    //    if (this.props.name !== "product_id") {
    //        return res;
    //    }

    //    const input = this?.autocomplete?.inputEl;
    //    console.log("INPUT TEST");
    //    console.log(input);
    //    if (input && !input._firstInputCaptured) {
    //        const self = this;
    //        input.addEventListener("input", function onInput() {
    //            if (!input._firstInputValueCaptured) {
    //                const value = input.value;
    //                console.log("First input value for product_id:", value);

    //                // Optionally: store it in a custom field, global, or state
    //                // self.props.record.update({ custom_product_search: value });

    //                input._firstInputValueCaptured = true; // prevent future captures
    //            }
    //        });

    //        input._firstInputCaptured = true;
    //    }
    ////    // Kun autocomplete aukeaa, input on olemassa -> liitetään kuuntelija
    ////    const test = attachInputListener(this);

    //    return res;
    //},

    //async _onProductUpdate() {
    //    const res = super._onProductUpdate(...arguments);
    //    console.log("PRODUCT UPDATE");
    //    console.log(res);
    //    const input = self?.autocomplete?.inputEl;
    //    console.log("PRODUCT INPUT");
    //    console.log(input);
    //    return res;
    //},

    //get productName() {
    //    const res = super.productName;
    //    //const res = super.productName(...arguments);
    //    console.log("PRODUCT NAME");
    //    console.log(res);
    //    return res;
    //},

    /* Kokeilu */
    //isSaleLineProductField(props) {
    //    return props?.name === "product_id" && props?.record?.model === "sale.order.line";
    //},

    //writeSearchTerm(record, term) {
    //    console.log("SEARCH TERM");
    //    console.log(term);
    //    if (record && typeof term === "string") {
    //        record.update({ product_search_term: term });
    //    }
    //},

    //attachInputListener(self) {
    //    console.log("TEST !!!! _____________-");
    //    // Liitetään input-kuuntelija kerran
    //    const input = self?.autocomplete?.inputEl;
    //    if (input && !input._rememberSearchAttached) {
    //        input.addEventListener("input", () => {
    //            if (isSaleLineProductField(self.props)) {
    //                writeSearchTerm(self.props.record, input.value || "");
    //            }
    //        });
    //        input._rememberSearchAttached = true;
    //    }
    //},
});

console.log("Patch applied to Many2OneField");

//class CustomSolProductMany2One extends SolProductMany2One {
//class SolProductMany2One extends SaleOrderLineProductField {
//    setup() {
//        super.setup();
//        this.state = useState({ searchTerm: "" });
//    }
//
//    _onProductSelected(product) {
//        super._onProductSelected(product);
//        this.state.searchTerm = product.display_name;
//        console.log("DISPLAY NAME");
//        console.log(product.display_name);
//        this._saveSearchTerm();
//    }
//
//    _saveSearchTerm() {
//        const { orderLine } = this.props;
//        orderLine.version_code_info = this.state.searchTerm;
//    }
//}
//
////registry.category("fields").add("sol_product_many2one", CustomSolProductMany2One);
//registry.category("fields").add("sol_product_many2one_extended", {
//  component: SolProductMany2One,
//});
//

//const container = document.querySelector('.o_field_many2one[data-name="product_template_id"]');
//if (!container) {
//    console.log("product_template_id container not found");
//} else {
//    console.log("product_template_id container found:", container);
//
//    const inputs = container.querySelectorAll('input');
//    console.log("Found inputs:", inputs);
//
//    const editables = container.querySelectorAll('[contenteditable="true"]');
//    console.log("Found contenteditable elements:", editables);
//
//    inputs.forEach(i => console.log("input value:", i.value));
//    editables.forEach(e => console.log("contenteditable text:", e.textContent));
//}
