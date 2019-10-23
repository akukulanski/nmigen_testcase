from nmigen import *
from nmigen.hdl.rec import Direction
from nmigen.cli import main
import os

class AxiStream(Record):
    def __init__(self, width, direction=None, name=None, fields=None):
        self.width = width
        self.DATA_FIELDS = [('TDATA', width)]
        if direction == 'sink':
            layout = [('TDATA', width, Direction.FANIN),
                      ('TVALID', 1, Direction.FANIN),
                      ('TREADY', 1, Direction.FANOUT),
                      ('TLAST', 1, Direction.FANIN)]
        elif direction == 'source':
            layout = [('TDATA', width, Direction.FANOUT),
                      ('TVALID', 1, Direction.FANOUT),
                      ('TREADY', 1, Direction.FANIN),
                      ('TLAST', 1, Direction.FANOUT)]
        Record.__init__(self, layout, name=name, fields=fields)

class DummyCore(Elaboratable):
    def __init__(self, width, testcase):
        self.input = AxiStream(width, 'sink', name='INPUT')
        self.output = AxiStream(width, 'source', name='OUTPUT')
        self.testcase = int(testcase)
    def elaborate(self, platform):
        m = Module()
        comb = m.d.comb
        if self.testcase == 0:
            comb += self.output.connect(self.input) # does not connect the signals
        elif self.testcase == 1:
            comb += self.input.connect(self.output) # does not connect the signals
        else:
            comb += self.output.TDATA.eq(self.input.TDATA)
            comb += self.output.TVALID.eq(self.input.TVALID)
            comb += self.output.TLAST.eq(self.input.TLAST)
            comb += self.input.TREADY.eq(self.output.TREADY)
        return m

if __name__ == '__main__':
    testcase = os.environ['TESTCASE']
    top = DummyCore(16, testcase)
    ports = [top.input[f] for f in top.input.fields]   
    ports += [top.output[f] for f in top.output.fields]
    main(top, ports=ports)