{
  'targets': [
    {
      'target_name': 'node_expat',
      'sources': [ 'node-expat.cc' ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      'cflags': [ "-Wno-cast-function-type", "-flto" ],
      'dependencies': [
        'deps/libexpat/libexpat.gyp:expat'
      ]
    }
  ]
}
