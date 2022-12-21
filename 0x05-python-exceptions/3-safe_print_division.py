#!/usr/bin/python3
def safe_print_division(a, b):
    ir = None
    try:
        ir = a / b
        print("Inside result: {:.1f}".format(ir))
    except Exception:
        print("Inside result: {}".format(ir))
        pass
    finally:
        return (ir)
