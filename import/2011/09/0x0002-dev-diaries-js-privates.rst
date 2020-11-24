A little experiment / toy I have, which I might use to keep some
decoupling attempts straight.
Using this, I'll be able to allow the various components to maintain
properties on other objects they work with, safely, without interfering
with one another.
For example, I have a Draggable behavior that can be enabled in a scene
and allows objects in the scene to be, obviously, draggable. During this
use, the behavior code may often need to set properties on the objects
to track dragging state, but needs to do so without interfering with
other behaviors setting properties of their own, even other instances of
the same behavior. This simple utility enables this.
privates(this, entity).dragPath = [];
privates(this, entity).dragPath.push(curPos);
...
drawPath(privates(this, entity).dragPath);
The concept this is trying to express is that the first object owns a
set of private properties attached to the second object, and this works
much like private attributes in many languages but works with delegation
and composition, rather than inheritance.
My rendering system will be using this to take the general description
of a sprite object and attach to it loaded images, animation state, and
flags needed to manage redraw orderings, without mucking in the
namespace of the object itself.
