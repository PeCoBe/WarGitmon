import argparse
import collections
import configparser
from datetime import datetime
import grp, pwd
from fnmatch import fnmatch
import hashlib
import hashlib
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(
    prog="WarGitmon",
    description="Content tracker for WarGreymon fans.",
    epilog="By PeCoBe, based on wyag.thb.lt")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"          | "Digivolve"       : cmd_add(args)
        case "cat-file"     | "DataScan"        : cmd_cat_file(args)
        case "check-ignore" | "ShieldGuard"     : cmd_check_ignore(args)
        case "checkout"     | "WarpDigivolve"   : cmd_checkout(args)
        case "commit"       | "Digitalize"      : cmd_commit(args)
        case "hash-object"  | "ChecksumCreate"  : cmd_hash_object(args)
        case "init"         | "Initialize"      : cmd_init(args)
        case "log"          | "DigiLog"         : cmd_log(args)
        case "ls-files"     | "ListFiles"       : cmd_ls_files(args)
        case "ls-tree"      | "DigiTree"        : cmd_ls_tree(args)
        case "rev-parse"    | "ParseRev"        : cmd_rev_parse(args)
        case "rm"           | "Deletion"        : cmd_rm(args)
        case "show-ref"     | "RefDisplay"      : cmd_show_ref(args)
        case "status"       | "DigiStatus"      : cmd_status(args)
        case "tag"          | "DigiTag"         : cmd_tag(args)
        case _              : print("Invalid Digi-command. Check your Digi-terminal.")