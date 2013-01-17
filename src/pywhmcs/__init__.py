import argparse
import logging as log


parser = argparse.ArgumentParser(description="pyWHMCS Client Comman Line Interface")
parser.add_argument("--debug", action="store_true", help="Activate debugging output")
parser.add_argument("--url", help="WHMCS API endpoint URL", required=True)
parser.add_argument("--username", help="Username with API permission", required=True)
parser.add_argument("--password", help="API user password", required=True)
parser.add_argument("--action", help="Action name to invoke", required=True)
parser.add_argument("--params", nargs=argparse.REMAINDER,
                    help="Parameters passed with action. (--params param1=value1 param2=value2 etc.)")
args = parser.parse_args()


def main():
    if args.debug:
        log.basicConfig(level=log.DEBUG)
    log.basicConfig(level=log.WARNING)

    log.info("Parameter List:")
    for k, v in args.__dict__.items():
        log.info("%s = %s" % (k.upper(), v))

    params_dict = {}
    for p in args.params:
        p_list = p.split('=')
        if len(p_list) != 2 or p_list[0] == "" or p_list[1] == "":
            log.info("Bad formatted --params: %s" % args.params)
            parser.error("Params bad format. Each param must be in param1=value1 format. Your data: %s" % p)
        params_dict[p_list[0]] = p_list[1]
    log.info("PARAMS dictionary: %s" % params_dict)

    invoke(args.url, args.username, args.password, args.action, params_dict)


def invoke(url, username, password, action, parameters):
    pass
