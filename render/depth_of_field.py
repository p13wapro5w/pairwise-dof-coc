import math

def coc_radius(depth, focus, aperture, sensor):
    """按深度与光圈计算 CoC 半径。"""
    raise NotImplementedError("TODO: coc_radius")

def half_res_extent(width, height):
    """半分辨率尺寸。"""
    raise NotImplementedError("TODO: half_res_extent")

def upsample_rect(x, y, scale):
    """上采样目标矩形。"""
    raise NotImplementedError("TODO: upsample_rect")

def focus_distance(near, far, t):
    """焦平面插值。"""
    raise NotImplementedError("TODO: focus_distance")

def premultiplied_depth(depth, alpha):
    """预乘深度。"""
    raise NotImplementedError("TODO: premultiplied_depth")

def clamp_coc(value, max_radius):
    """CoC 半径钳制。"""
    raise NotImplementedError("TODO: clamp_coc")

def bokeh_weight(total):
    """单采样能量权重。"""
    raise NotImplementedError("TODO: bokeh_weight")

def soft_clip(value, limit):
    """近平面软饱和。"""
    raise NotImplementedError("TODO: soft_clip")

def hdr_linear(channel, exposure):
    """线性 HDR 亮度。"""
    raise NotImplementedError("TODO: hdr_linear")

def camera_key(camera_id, frame):
    """相机历史键。"""
    raise NotImplementedError("TODO: camera_key")

def reset_history(focus_changed, cut):
    """是否重置景深历史。"""
    raise NotImplementedError("TODO: reset_history")

def kernel_scale(resolution, base):
    """kernel 分辨率缩放。"""
    raise NotImplementedError("TODO: kernel_scale")

def aperture_blades(blades, samples):
    """光圈叶片与采样。"""
    raise NotImplementedError("TODO: aperture_blades")

def dof_blend(sharp, blurred, weight):
    """景深混合。"""
    raise NotImplementedError("TODO: dof_blend")

def focus_transition(current, target, step):
    """焦距平滑。"""
    raise NotImplementedError("TODO: focus_transition")
