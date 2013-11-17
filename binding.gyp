{
    "targets": [{
      "target_name": "leveldown"
    , "conditions": [
        ['OS == "linux"', {
            'cflags': [
                '-Wno-unused-local-typedefs',
                '-pthread',
                '-m64',
                '-Wall', 
                '-Wextra', 
                '-Wno-unused-parameter',
            ],            
            'ldflags': [ '-pthread', '-m64', '-rdynamic'],
            'cflags_cc': [ '-fno-rtti', '-fno-exceptions' ],
            'target_conditions': [
                ['_type=="static_library"', {
                    'standalone_static_library': 1, # disable thin archive which needs binutils >= 2.19
                }],
                ]
        }]

        ]
      , "dependencies": [
            "<(module_root_dir)/deps/leveldb/leveldb.gyp:leveldb"
        ]
      , "include_dirs"  : [
            "<!(node -e \"require('nan')\")"
        ]
      , "sources": [
            "src/batch.cc"
          , "src/batch_async.cc"
          , "src/database.cc"
          , "src/database_async.cc"
          , "src/iterator.cc"
          , "src/iterator_async.cc"
          , "src/leveldown.cc"
          , "src/leveldown_async.cc"
        ]
    },
    {
        'target_name': 'c_unit_test',
        'type': 'executable',
        'include_dirs': [
          '.',
        ],
        'dependencies': [
                      'deps/v8/tools/gyp/v8.gyp:v8'
                      ],
        'sources': [
          'src/test.cc',
        ],
      }
    ], 

}
