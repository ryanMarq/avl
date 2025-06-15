typedef struct packed {
  logic        sign;
  logic [4:0]  exponent;
  logic [9:0]  mantissa;
} fp16_t;


typedef struct packed {
  logic        sign;
  logic [7:0]  exponent;
  logic [22:0] mantissa;
} fp32_t;

typedef struct packed {
  logic        sign;
  logic [10:0] exponent;
  logic [51:0] mantissa;
} fp64_t;

module example_hdl();

    logic        clk;
    logic        rst_n;

    fp16_t       fp16;
    fp32_t       fp32;
    fp64_t       fp64;

endmodule : example_hdl
