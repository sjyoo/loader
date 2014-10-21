/*
Loader APIs 


*/

module Loader 
{
    /*You need to use KBase auth service to get the authentication*/
    authentication required;
  
    /* A type string copied from WS spec.
         Specifies the type and its version in a single string in the format
         [module].[typename]-[major].[minor]:
         
         module - a string. The module name of the typespec containing the type.
         typename - a string. The name of the type as assigned by the typedef
                 statement. For external type, it start with “e_”.
         major - an integer. The major version of the type. A change in the
                 major version implies the type has changed in a non-backwards
                 compatible way.
         minor - an integer. The minor version of the type. A change in the
                 minor version implies that the type has changed in a way that is
                 backwards compatible with previous type definitions.
         
         In many cases, the major and minor versions are optional, and if not
         provided the most recent version will be used.
         
         Example: MyModule.MyType-3.1
  */
  typedef string type_string;
  
  
      typedef string shock_id;
  
      /* optional shock_url */
      typedef structure {
          typedef shock_id id;
          typedef string shock_url;
      } shock_ref;
  
  /* Information about a module copied from WS.
          
          list<username> owners - the owners of the module.
          spec_version ver - the version of the module.
          typespec spec - the typespec.
          string description - the description of the module from the typespec.
          mapping<type_string, jsonschema> types - the types associated with this
                  module and their JSON schema.
          mapping<modulename, spec_version> included_spec_version - names of 
                  included modules associated with their versions.
          string chsum - the md5 checksum of the object.
          list<func_string> functions - list of names of functions registered in spec.
          boolean is_released - shows if this version of module was released (and hence can be seen by others).
  */
  typedef structure {
          list<username> owners;
          spec_version ver;
          typespec spec;
          string description;
          mapping<type_string, jsonschema> types;
          mapping<type_string, shock_ref> etypes;
          mapping<type_string, shock_ref> validators; /* etype validators script reference in shock*/
          mapping<type_string, shock_ref> transformers; /* etype translators script reference in shock*/
          mapping<type_string, shock_ref> importer; /* etype importer script reference in shock*/
  
          mapping<modulename, spec_version> included_spec_version;
          string chsum;
          list<func_string> functions;
          boolean is_released;
  } ModuleInfo;
  
  
  typedef structure {
      typedef type_string etype;
      typedef string default_source_url;
      typedef shock_ref script;
  } Importer;
  
  funcdef request_to_register_importer(Importer) returns (string result);
  
  funcdef release_ importer(Importer) return (string result);
  
  funcdef import(ext_type, string url) return (string result);
  
  
  
  typedef structure {
      typedef type_string etype;
      typedef shock_ref validation_script;
  } Validator;
  
  funcdef request_to_register_validator(Validator) returns (string result);
  
  funcdef release_validator(Validator) return (string result);
  
  funcdef validate(type_string ext_type, shock_ref id) return (string result);
  
  
  
  typedef structure {
      typedef Validator validator;
      typedef type_string kb_type;
      typedef shock_ref translation_script;
  } Uploader;
  
  funcdef request_to_register_uploader(Uploader) returns (string result);
  
  funcdef release_uploader(Uploader) return (string result);
  
  funcdef uploader(type_string ext_type, type_string kb_type, shock_ref in_id, string ws_out_id, string out_obj_id) return (string result);     
  
  typedef structure {
      typedef type_string kb_type;
      typedef type_string ext_type;
      typedef shock_ref translation_script;
  } Downloader;
  
  funcdef request_to_register_downloader(Downloader) return (string url);
  funcdef release_downloader(Downloader) return (string url);
  funcdef download(type_string ext_type, ws_out_id, string ou_obj_id) return (string url);
  
};
