#include "config.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct
{
    char *key;
    char *value;
} ConfigEntry;

struct Config
{
    ConfigEntry *entries;
    size_t count;
};

static char *strdup_safe(const char *s)
{
    size_t len = strlen(s);

    char *copy = malloc(len + 1);

    if (!copy)
        return NULL;

    memcpy(copy, s, len + 1);

    return copy;
}

char *trim(char *str)
{
    while (isspace((unsigned char)*str))
        str++;

    if (*str == '\0')
        return str;

    char *end = str + strlen(str) - 1;

    while (end > str &&
           isspace((unsigned char)*end))
    {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

void strip_quotes(char *str)
{
    size_t len = strlen(str);

    if (len >= 2 &&
        (str[0] == '"' || str[0] == '\'') &&
        str[len - 1] == str[0])
    {
        memmove(str, str + 1, len - 2);
        str[len - 2] = '\0';
    }
}

Config *config_load(const char *filename)
{
    FILE *file = fopen(filename, "r");

    if (!file)
        return NULL;

    Config *cfg = calloc(1, sizeof(Config));

    if (!cfg)
    {
        fclose(file);
        return NULL;
    }

    char line[512];

    while (fgets(line, sizeof(line), file))
    {
        line[strcspn(line, "\r\n")] = '\0';

        if (line[0] == '\0' || line[0] == '#')
            continue;

        char *eq = strchr(line, '=');

        if (!eq)
            continue;

        *eq = '\0';

        char *key = trim(line);
        char *value = trim(eq + 1);
        strip_quotes(value);

        ConfigEntry *tmp =
            realloc(cfg->entries,
                    (cfg->count + 1)
                    * sizeof(ConfigEntry));

        if (!tmp)
        {
            config_free(cfg);
            fclose(file);
            return NULL;
        }

        cfg->entries = tmp;

        cfg->entries[cfg->count].key =
            strdup_safe(key);

        cfg->entries[cfg->count].value =
            strdup_safe(value);

        if (!cfg->entries[cfg->count].key ||
            !cfg->entries[cfg->count].value)
        {
            config_free(cfg);
            fclose(file);
            return NULL;
        }

        cfg->count++;
    }

    fclose(file);

    return cfg;
}

const char *config_get(
    const Config *cfg,
    const char *key)
{
    if (!cfg || !key)
        return NULL;

    for (size_t i = 0; i < cfg->count; i++)
    {
        if (strstr(cfg->entries[i].key, key))
        {
            return cfg->entries[i].value;
        }
    }

    return NULL;
}

void config_free(Config *cfg)
{
    if (!cfg)
        return;

    for (size_t i = 0; i < cfg->count; i++)
    {
        free(cfg->entries[i].key);
        free(cfg->entries[i].value);
    }

    free(cfg->entries);
    free(cfg);
}