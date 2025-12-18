import { styled } from "@mui/material/styles";
import { Stack } from "@mui/material";

export const StyledContainer = styled(Stack)(({ theme }) => ({
    background: theme.custom.background,
    height: "100vh",
    "& .body": {
        padding: "0 25px",
        gap: "15px",
        "& h6": { textAlign: "center" },
        "& .form": {
            gap: "10px",
            flexDirection: "row",
        }
    }
}))