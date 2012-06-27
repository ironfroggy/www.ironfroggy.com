Python developers commonly ask for an easy way to implement "plug-ins" and
`straight.plugin` offers that in a very easy interface, which builds on top
of namespace packages. A simple call to ``load("my.namespace")`` will load
any modules under the package ``my.namespace`` and options are also
provided to locate and filter classes or objects inside the modules by
type.
