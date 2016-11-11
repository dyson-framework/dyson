Modules
=======

Modules are the backbone to Dyson.  Modules represent specific steps
that are able to be executed within tests.

There are two repositories that house Dyson's modules.  These repositories are

- [Dyson Core Modules](https://github.com/dynamictivity/dyson-modules-core)
- [Dyson Extra Modules](https://github.com/dynamictivity/dyson-modules-extras)

---

Table of Contents

- [Core Modules](#dyson-core-modules)
- [Extra Modules](#dyson-extra-modules)
- [Module Overriding](#dyson-module-overriding)
- [Creating Modules](https://github.com/dynamictivity/dyson/tree/docs/creating_modules.md)


## Dyson Core Modules

The core modules that are included with Dyson are those that are primarily
related to the operation of selenium.

These modules include specific [actions](https://github.com/dynamictivity/dyson/tree/master/docs/actions.md) that can be performed with Selenium,
and [validations](https://github.com/dynamictivity/dyson/tree/master/docs/validations.md) that can be performed by Dyson

## Dyson Extra Modules

The extra modules included with Dyson are modules that aren't pertinent to the operation of Dyson.

In this repository, you will find "helpful" steps, or "sugar" steps that make Dyson easier to use.

## Module Overriding

As per the whole idea with Dyson - you are able to override pretty much *everything*.  This includes overriding core modules.

Let's say that you need to override the `click` module, as it doesn't operate as you'd expect.
You can create `click.py` in the `modules` directory, and follow the [guidelines](https://github.com/dynamictivity/dyson/tree/docs/creating_modules.md) on creating a module
to customize your module to do as you wish.

There are times where you might to override a module to wait for an element before interacting with it.  For this, you want
to utilize [keywords](https://github.com/dynamictivity/dyson/tree/master/docs/keywords.md).

## Creating Modules

> [See Creating Modules](https://github.com/dynamictivity/dyson/tree/master/docs/creating_modules.md)
