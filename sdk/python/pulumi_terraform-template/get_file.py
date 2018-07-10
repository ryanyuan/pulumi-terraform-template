# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetFileResult(object):
    """
    A collection of values returned by getFile.
    """
    def __init__(__self__, rendered=None, id=None):
        if rendered and not isinstance(rendered, basestring):
            raise TypeError('Expected argument rendered to be a basestring')
        __self__.rendered = rendered
        """
        The final rendered template.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_file(filename=None, template=None, vars=None):
    """
    Renders a template from a file.
    """
    __args__ = dict()

    __args__['filename'] = filename
    __args__['template'] = template
    __args__['vars'] = vars
    __ret__ = pulumi.runtime.invoke('terraform-template:index/getFile:getFile', __args__)

    return GetFileResult(
        rendered=__ret__.get('rendered'),
        id=__ret__.get('id'))