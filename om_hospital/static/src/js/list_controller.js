/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";
import { useService} from "@web/core/utils/hooks";

patch(ListController.prototype, "om_patient",{
    setup(){
        this._super.apply();
        this.action = useService("action")
    },
    omButtonClickEvent(){
        this.action.doAction({
            type:"ir.actions.act_window",
            name:"Add Appointment",
            res_model:"hospital.appointment",
            target:"new",
            views:[[false, "form"]],
            view_mode:"form",
        });
    }
});