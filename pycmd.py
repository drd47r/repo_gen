#!/usr/bin/env python3
import argparse

import cmd2
from cmd2 import Cmd
from cmd2 import with_argparser

from lab import Laboratory


class bREPL(Cmd):
    """
    Read Eval Print Loop for bob
    """
    prompt = "Bots> "
    intro = "Welcome for emulation bots' REPL"

    argparser_run = argparse.ArgumentParser()
    argparser_run.add_argument('-p', "--path_dump_data",
                           help='set path in there we store dumped data')

    argparser_run.add_argument('-s', "--need_save",
                           action='store_true',
                           default=False,
                           help='save dumped data')

    argparser_show = argparse.ArgumentParser()
    argparser_show.add_argument('dumpfile', nargs='+',
                           help='give dumpfile')

    def __init__(self):
        Cmd.__init__(self)
        self.l = Laboratory()

    @with_argparser(argparser_run)
    def do_run(self, line):
        if line.path_dump_data:
            self.l.setdumppath(line.path_dump_data)
        self.l.mainprocess()
        self.l.showresult()
        if line.need_save:
            self.l.dumpresult()

    @with_argparser(argparser_show)
    def do_show(self, line):
        if not line.dumpfile:
            print("we need a file name to load")
            return
        self.l.loadresult(line.dumpfile[0])
        self.l.showresult()

    def complete_show(self, text, line, start_index, end_index):
        return cmd2.path_complete(text, line, start_index, end_index)

if __name__ == '__main__':
    app = bREPL()
    app.cmdloop()
