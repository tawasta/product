from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    """Recompute the template delivery package flag.

    In 17.0 the stored value was computed only when the template was created,
    so existing templates can have an outdated value."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    templates = env["product.template"].with_context(active_test=False).search([])
    env.add_to_compute(templates._fields["is_delivery_package"], templates)
    templates.flush_recordset(["is_delivery_package"])
