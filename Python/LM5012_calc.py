
import math
def buckcalculations():
  v_out = 5
  r_on = 41.2e3
  f_sw = 1e3 * (v_out * 2500) / (r_on/1e3)
  t_min = 50e-9
  d_min = t_min * f_sw
  v_in_max = v_out/(t_min * f_sw)
  v_in = 84
  I_out_max = 2.5
  L_o = 40e-6
  delta_I_l = v_out/(f_sw * L_o) * (1 - v_out/v_in)
  I_l_peak = I_out_max + delta_I_l/2
  C_out_min = delta_I_l / (8 * f_sw * v_out * .005)
  D = v_out/v_in
  # V_in_ripple = I_out_max * D * (1-D) / (f_sw * c_)
  print(I_l_peak)

def ledcalculations():
  v_out = 12
  v_in = 84
  i_led = 1
  f_s = 1.25e6
  c_in = 4.7e-6
  I_d = i_led * math.sqrt(v_out/v_in)
  delta_v_in = i_led / (f_s * c_in) * v_out / v_in * (1 - v_out/v_in)
  print(delta_v_in)
ledcalculations()