import pytest
from render import depth_of_field as mod

CASES = [
    ("coc", 'm.coc_radius(20, 10, 2, 0.5) == approx(0.5)'),
    ("half", 'm.half_res_extent(7, 5) == (4, 3)'),
    ("rect", 'm.upsample_rect(2, 3, 2) == (4, 6, 2, 2)'),
    ("focus", 'm.focus_distance(2, 10, 0.5) == approx(6.0)'),
    ("premult", 'm.premultiplied_depth(0.5, 0.4) == approx(0.2)'),
    ("clamp", 'm.clamp_coc(-3, 2) == approx(2.0)'),
    ("weight", 'm.bokeh_weight(4) == approx(0.25)'),
    ("clip", 'm.soft_clip(5, 3) == approx(3.0)'),
    ("hdr", 'm.hdr_linear(0.5, 2) == approx(1.0)'),
    ("key", 'm.camera_key("camL", 7) == "camL:7"'),
    ("reset", 'm.reset_history(True, False) is True'),
    ("kernel", 'm.kernel_scale(2160, 1080) == approx(2.0)'),
    ("blades", 'm.aperture_blades(9, 6) == 6'),
    ("blend", 'm.dof_blend(2, 4, 0.5) == approx(3.0)'),
    ("transition", 'm.focus_transition(0, 10, 3) == approx(3.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
