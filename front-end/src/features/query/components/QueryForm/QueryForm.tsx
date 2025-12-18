import { Controller, FormProvider, useForm } from "react-hook-form";
import { StyledContainer } from "./queryForm.styles";
import type { QueryFormComponent } from "./queryForm.types";
import Input from "../../../../shared/components/Input/Input";
import type { QueryFormData } from "../../types";
import { useEffect, useState } from "react";
import useQuery from "../../hooks/useQuery";
import { Autocomplete } from "@mui/material";

const QueryForm: QueryFormComponent = ({ onDomainChange }) => {
  const [suggestions, setSuggestions] = useState<string[]>([]);

  const methods = useForm<QueryFormData>();
  const query = methods.watch("query");
  const { sendQuery } = useQuery();

  useEffect(() => {
    const updateSuggestions = async () => {
      if (query?.length) {
        const q = query.split(" ")?.pop() || "";
        if (q.length > 0) {
          const { suggestions: sugg, domain: dom } = await sendQuery({
            query: q,
          });
          setSuggestions(sugg);
          onDomainChange(dom);
        }
      }
    };
    updateSuggestions();
  }, [query]);

  useEffect(() => {
    console.log(suggestions);
  }, [suggestions]);

  return (
    <StyledContainer>
      <FormProvider {...methods}>
        <Controller
          name="query"
          control={methods.control}
          render={({ field }) => (
            <Autocomplete
              freeSolo
              disableClearable
              filterOptions={(x) => x}
              options={suggestions}
              onInputChange={(_, value) => field.onChange(value)}
              renderInput={(params) => (
                <Input
                  {...field}
                  {...params}
                  inputRef={params.InputProps.ref}
                />
              )}
            />
          )}
        />
      </FormProvider>
    </StyledContainer>
  );
};

export default QueryForm;
