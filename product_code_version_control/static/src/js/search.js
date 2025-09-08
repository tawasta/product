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

patch(SaleOrderLineProductField.prototype, {
    get Many2XAutocompleteProps() {
        const props = super.Many2XAutocompleteProps;
        //const props = super.Many2XAutocompleteProps(...arguments);
        console.log("Many2XAutocompleteProps on SO line:", props);
        //const focus = this.autocompleteContainerRef.el.querySelector("input").focus();
        const input = self;
        console.log("INPUT AUTOCOMPLETE", input);
        //console.log("INPUT", input);

        return props;
    },

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
});
