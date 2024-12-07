name = "karpenter"
version = "1.0.0"
author = "felix benicourt"

build_command = False
requires = ['python-3.10', 'hal_server-1.0.0']

def commands():
    env.PYTHONPATH.append(this.root)
    env.PYTHONPATH.append("{root}/karpenter")
    env.PATH.append(this.root)
    env.PATH.append("{root}/karpenter")
    alias("karpenter", "python {root}/karpenter/main.py")