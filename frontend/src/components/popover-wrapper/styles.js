import { makeStyles } from '@material-ui/core/styles';

export const useStyles = makeStyles((theme) => ({
  popover: {
    pointerEvents: 'none',
  },
  paper: {
    padding: theme.spacing(1),
    maxWidth: '500px',
  },
  children: {
    display: 'flex',
    '&:hover': {
      cursor: 'pointer',
    },
  },
}));
