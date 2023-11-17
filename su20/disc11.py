def make_lambda(params, body):
    """
    >>> g = make_lambda("a, b, c", "c if a > b else -c")
    >>> g(1, 2, 3)
    -3
    """
    # s = f'lambda {params}: {body}'
    # `(lambda (,params) ,body)
    s = 'lambda ' + params + ': ' + body
    return eval(s)
    
