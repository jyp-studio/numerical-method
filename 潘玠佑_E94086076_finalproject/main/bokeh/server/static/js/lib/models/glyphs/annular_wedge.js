var _a;
import { XYGlyph, XYGlyphView } from "./xy_glyph";
import { generic_area_vector_legend } from "./utils";
import { LineVector, FillVector, HatchVector } from "../../core/property_mixins";
import { to_screen } from "../../core/types";
import { Direction } from "../../core/enums";
import * as p from "../../core/properties";
import { angle_between } from "../../core/util/math";
import { Selection } from "../selections/selection";
import { max } from "../../core/util/arrayable";
export class AnnularWedgeView extends XYGlyphView {
    _map_data() {
        if (this.model.properties.inner_radius.units == "data")
            this.sinner_radius = this.sdist(this.renderer.xscale, this._x, this.inner_radius);
        else
            this.sinner_radius = to_screen(this.inner_radius);
        if (this.model.properties.outer_radius.units == "data")
            this.souter_radius = this.sdist(this.renderer.xscale, this._x, this.outer_radius);
        else
            this.souter_radius = to_screen(this.outer_radius);
        this.max_souter_radius = max(this.souter_radius);
    }
    _render(ctx, indices, data) {
        const { sx, sy, start_angle, end_angle, sinner_radius, souter_radius } = data ?? this;
        const anticlock = this.model.direction == "anticlock";
        for (const i of indices) {
            const sx_i = sx[i];
            const sy_i = sy[i];
            const sinner_radius_i = sinner_radius[i];
            const souter_radius_i = souter_radius[i];
            const start_angle_i = start_angle.get(i);
            const end_angle_i = end_angle.get(i);
            if (!isFinite(sx_i + sy_i + sinner_radius_i + souter_radius_i + start_angle_i + end_angle_i))
                continue;
            const angle_i = end_angle_i - start_angle_i;
            ctx.translate(sx_i, sy_i);
            ctx.rotate(start_angle_i);
            ctx.beginPath();
            ctx.moveTo(souter_radius_i, 0);
            ctx.arc(0, 0, souter_radius_i, 0, angle_i, anticlock);
            ctx.rotate(angle_i);
            ctx.lineTo(sinner_radius_i, 0);
            ctx.arc(0, 0, sinner_radius_i, 0, -angle_i, !anticlock);
            ctx.closePath();
            ctx.rotate(-angle_i - start_angle_i);
            ctx.translate(-sx_i, -sy_i);
            this.visuals.fill.apply(ctx, i);
            this.visuals.hatch.apply(ctx, i);
            this.visuals.line.apply(ctx, i);
        }
    }
    _hit_point(geometry) {
        const { sx, sy } = geometry;
        const x = this.renderer.xscale.invert(sx);
        const y = this.renderer.yscale.invert(sy);
        // check radius first
        const sx0 = sx - this.max_souter_radius;
        const sx1 = sx + this.max_souter_radius;
        const [x0, x1] = this.renderer.xscale.r_invert(sx0, sx1);
        const sy0 = sy - this.max_souter_radius;
        const sy1 = sy + this.max_souter_radius;
        const [y0, y1] = this.renderer.yscale.r_invert(sy0, sy1);
        const candidates = [];
        for (const i of this.index.indices({ x0, x1, y0, y1 })) {
            const or2 = this.souter_radius[i] ** 2;
            const ir2 = this.sinner_radius[i] ** 2;
            const [sx0, sx1] = this.renderer.xscale.r_compute(x, this._x[i]);
            const [sy0, sy1] = this.renderer.yscale.r_compute(y, this._y[i]);
            const dist = (sx0 - sx1) ** 2 + (sy0 - sy1) ** 2;
            if (dist <= or2 && dist >= ir2)
                candidates.push(i);
        }
        const anticlock = this.model.direction == "anticlock";
        const indices = [];
        for (const i of candidates) {
            // NOTE: minus the angle because JS uses non-mathy convention for angles
            const angle = Math.atan2(sy - this.sy[i], sx - this.sx[i]);
            if (angle_between(-angle, -this.start_angle.get(i), -this.end_angle.get(i), anticlock)) {
                indices.push(i);
            }
        }
        return new Selection({ indices });
    }
    draw_legend_for_index(ctx, bbox, index) {
        generic_area_vector_legend(this.visuals, ctx, bbox, index);
    }
    scenterxy(i) {
        const r = (this.sinner_radius[i] + this.souter_radius[i]) / 2;
        const a = (this.start_angle.get(i) + this.end_angle.get(i)) / 2;
        const scx = this.sx[i] + r * Math.cos(a);
        const scy = this.sy[i] + r * Math.sin(a);
        return [scx, scy];
    }
}
AnnularWedgeView.__name__ = "AnnularWedgeView";
export class AnnularWedge extends XYGlyph {
    constructor(attrs) {
        super(attrs);
    }
}
_a = AnnularWedge;
AnnularWedge.__name__ = "AnnularWedge";
(() => {
    _a.prototype.default_view = AnnularWedgeView;
    _a.mixins([LineVector, FillVector, HatchVector]);
    _a.define(({}) => ({
        direction: [Direction, "anticlock"],
        inner_radius: [p.DistanceSpec, { field: "inner_radius" }],
        outer_radius: [p.DistanceSpec, { field: "outer_radius" }],
        start_angle: [p.AngleSpec, { field: "start_angle" }],
        end_angle: [p.AngleSpec, { field: "end_angle" }],
    }));
})();
//# sourceMappingURL=annular_wedge.js.map