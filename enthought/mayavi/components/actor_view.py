"""
Traits View definition file.

The view trait of the parent class is extracted from the model definition 
file.  This file can either be exec()ed or imported.  See 
core/base.py:Base.trait_view() for what is currently used.  Using exec() 
allows view changes without needing to restart Mayavi, but is slower than 
importing.
"""
# Authors: Prabhu Ramachandran <prabhu_r@users.sf.net>
#          Judah De Paula <judah@enthought.com>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

from enthought.traits.ui.api import View, Group, Item, InstanceEditor, DropEditor
from enthought.tvtk.api import tvtk

VTK_VER = tvtk.Version().vtk_version

# The properties view group.
_prop_group = Group(Item(name='representation'),
                    Item(name='color'),
                    Item(name='line_width'),
                    Item(name='point_size'),
                    Item(name='opacity'),
                    show_border=True,
                    label='Property'
                    )

# The mapper's view group.
if VTK_VER[:3] in ['4.2', '4.4']:
    _mapper_group = Group(Item(name='scalar_visibility'),
                          show_border=True, label='Mapper')
else:
    _mapper_group = Group(Item(name='scalar_visibility'),
                          Item(name='interpolate_scalars_before_mapping'),
                          show_border=True, label='Mapper')

# The Texture's view group
_texture_group = Group(Item(name='interpolate'),
                       Item(name='map_color_scalars_through_lookup_table'),
                       Item(name='repeat'),
                       show_border=True,
                       #label='Texture',
                       )
   
# The Actor's view group.
_actor_group = Group(Item(name='visibility'),
                     show_border=True, label='Actor')

actor_group = Group(Item(name='actor', style='custom',
                       editor=InstanceEditor(view=View(_actor_group))),
                    Item(name='mapper', style='custom',
                       editor=InstanceEditor(view=View(_mapper_group))),
                    Item(name='property', style='custom',
                       editor=InstanceEditor(view=View(_prop_group))),
                    show_labels=False,
                    )

texture_group = Group(Item(name='enable_texture'),
                  Group(Item(name='texture_source_object' , style='custom',editor=DropEditor()),
                        Item(name='texture',style='custom',
                             editor=InstanceEditor(view=View(_texture_group))),
                        show_labels=True,
                        label='Texture Properties',
                        enabled_when='object.enable_texture',
                        show_border=True),
                )


# The Views for this object.  Pick the one that you need.
actor_view = View(actor_group, resizable=True)
texture_view = View(texture_group, resizable=True)
view = View(actor_group, texture_group, resizable=True)
