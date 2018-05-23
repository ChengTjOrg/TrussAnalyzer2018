import PostProcess

def fig():
    data=PostProcess.PostProcess(6)
    data.loadtruss()
    data.setfig()
    data.plot()
    data.savefig()

fig()