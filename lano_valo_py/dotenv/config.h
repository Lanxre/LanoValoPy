#ifndef CONFIG_H
#define CONFIG_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct Config Config;

Config *config_load(const char *filename);

const char *config_get(
    const Config *cfg,
    const char *key
);

void config_free(Config *cfg);

#ifdef __cplusplus
}
#endif

#endif