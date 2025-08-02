
typedef enum logic [1:0] {
    S0 = 2'b00,
    S1 = 2'b01,
    S2 = 2'b10
} state_t;

typedef struct packed {
    logic        single_bit;
    logic [31:0] multi_bit;
    state_t      state_enum;
} packed_struct_t;

module example_hdl();

    logic        clk;
    logic        rst_n;
    packed_struct_t data;

endmodule : example_hdl
