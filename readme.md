
## Issue testcase

Issue: https://github.com/m-labs/nmigen/issues/257


### Testcases

**Case 0**:
```verilog
comb += self.output.connect(self.input)
```

**Case 1**:
```verilog
comb += self.input.connect(self.output)
```

**Case_2**:
```verilog
comb += self.output.TDATA.eq(self.input.TDATA)
comb += self.output.TVALID.eq(self.input.TVALID)
comb += self.output.TLAST.eq(self.input.TLAST)
comb += self.input.TREADY.eq(self.output.TREADY)
```

### Generate verilog files

```bash
export TESTCASE=0
python3 ./test_case.py generate > case_$TESTCASE.v
export TESTCASE=1
python3 ./test_case.py generate > case_$TESTCASE.v
export TESTCASE=2
python3 ./test_case.py generate > case_$TESTCASE.v
```

### Output files

*case_0.v* and *case_1.v* are exactly the same, and with the signals inverted with respect to *case_2.v*.



case_0.v:
```verilog
/* Generated by Yosys 0.9+932 (git sha1 4072a966, gcc 7.4.0-1ubuntu1~18.04.1 -fPIC -Os) */

(* generator = "nMigen" *)
(* top =  1  *)
(* \nmigen.hierarchy  = "top" *)
module top(INPUT__TVALID, INPUT__TREADY, INPUT__TLAST, OUTPUT__TDATA, OUTPUT__TVALID, OUTPUT__TREADY, OUTPUT__TLAST, INPUT__TDATA);
  (* src = "./test_case.py:20" *)
  output [15:0] INPUT__TDATA;
  (* src = "./test_case.py:20" *)
  output INPUT__TLAST;
  (* src = "./test_case.py:20" *)
  input INPUT__TREADY;
  (* src = "./test_case.py:20" *)
  output INPUT__TVALID;
  (* src = "./test_case.py:20" *)
  input [15:0] OUTPUT__TDATA;
  (* src = "./test_case.py:20" *)
  input OUTPUT__TLAST;
  (* src = "./test_case.py:20" *)
  output OUTPUT__TREADY;
  (* src = "./test_case.py:20" *)
  input OUTPUT__TVALID;
  assign INPUT__TLAST = OUTPUT__TLAST;
  assign OUTPUT__TREADY = INPUT__TREADY;
  assign INPUT__TVALID = OUTPUT__TVALID;
  assign INPUT__TDATA = OUTPUT__TDATA;
endmodule
```

case_1.v:
```verilog
/* Generated by Yosys 0.9+932 (git sha1 4072a966, gcc 7.4.0-1ubuntu1~18.04.1 -fPIC -Os) */

(* generator = "nMigen" *)
(* top =  1  *)
(* \nmigen.hierarchy  = "top" *)
module top(INPUT__TVALID, INPUT__TREADY, INPUT__TLAST, OUTPUT__TDATA, OUTPUT__TVALID, OUTPUT__TREADY, OUTPUT__TLAST, INPUT__TDATA);
  (* src = "./test_case.py:20" *)
  output [15:0] INPUT__TDATA;
  (* src = "./test_case.py:20" *)
  output INPUT__TLAST;
  (* src = "./test_case.py:20" *)
  input INPUT__TREADY;
  (* src = "./test_case.py:20" *)
  output INPUT__TVALID;
  (* src = "./test_case.py:20" *)
  input [15:0] OUTPUT__TDATA;
  (* src = "./test_case.py:20" *)
  input OUTPUT__TLAST;
  (* src = "./test_case.py:20" *)
  output OUTPUT__TREADY;
  (* src = "./test_case.py:20" *)
  input OUTPUT__TVALID;
  assign INPUT__TLAST = OUTPUT__TLAST;
  assign OUTPUT__TREADY = INPUT__TREADY;
  assign INPUT__TVALID = OUTPUT__TVALID;
  assign INPUT__TDATA = OUTPUT__TDATA;
endmodule
```

case_2.v:
```verilog
/* Generated by Yosys 0.9+932 (git sha1 4072a966, gcc 7.4.0-1ubuntu1~18.04.1 -fPIC -Os) */

(* generator = "nMigen" *)
(* top =  1  *)
(* \nmigen.hierarchy  = "top" *)
module top(INPUT__TVALID, INPUT__TREADY, INPUT__TLAST, OUTPUT__TDATA, OUTPUT__TVALID, OUTPUT__TREADY, OUTPUT__TLAST, INPUT__TDATA);
  (* src = "./test_case.py:20" *)
  input [15:0] INPUT__TDATA;
  (* src = "./test_case.py:20" *)
  input INPUT__TLAST;
  (* src = "./test_case.py:20" *)
  output INPUT__TREADY;
  (* src = "./test_case.py:20" *)
  input INPUT__TVALID;
  (* src = "./test_case.py:20" *)
  output [15:0] OUTPUT__TDATA;
  (* src = "./test_case.py:20" *)
  output OUTPUT__TLAST;
  (* src = "./test_case.py:20" *)
  input OUTPUT__TREADY;
  (* src = "./test_case.py:20" *)
  output OUTPUT__TVALID;
  assign INPUT__TREADY = OUTPUT__TREADY;
  assign OUTPUT__TLAST = INPUT__TLAST;
  assign OUTPUT__TVALID = INPUT__TVALID;
  assign OUTPUT__TDATA = INPUT__TDATA;
endmodule
```