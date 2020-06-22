import React from 'react';

import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from '@material-ui/core';
import Slider from '@material-ui/core/Slider';
import Tooltip from '@material-ui/core/Tooltip';

import useStyles from './styles';

function ValueLabelComponent(props) {
  const { children, open, value } = props;

  return (
    <Tooltip open={open} enterTouchDelay={0} placement="top" title={value}>
      {children}
    </Tooltip>
  );
}

ValueLabelComponent.propTypes = {
  children: PropTypes.element.isRequired,
  open: PropTypes.bool.isRequired,
  value: PropTypes.number.isRequired,
};

const PrettoSlider = withStyles({
  root: {
    color: '#012934',
    height: 8,
  },
  thumb: {
    color: '#012934',
    height: 24,
    width: 24,
    backgroundColor: '#fff',
    border: '2px solid currentColor',
    marginTop: -8,
    marginLeft: -12,
    '&:focus, &:hover, &$active': {
      boxShadow: 'inherit',
    },
  },
  active: {},
  valueLabel: {
    left: 'calc(-50% + 4px)',
  },
  track: {
    color: '#012934',
    height: 8,
    borderRadius: 4,
  },
  rail: {
    height: 8,
    borderRadius: 4,
  },
})(Slider);

const CustomSliderField = ({
  input,
  value,
  onChange,
  ariaLabelledBy,
  classStyle,
}) => {
  const classes = useStyles();
  const [min, setMin] = React.useState(
    ariaLabelledBy ? Math.min(...input.value) : 0
  );
  const [max, setMax] = React.useState(
    ariaLabelledBy ? Math.max(...input.value) : 10
  );
  const handleInputChange = (newValue) => {
    input.onChange(newValue);
  };

  return (
    <div className={classNames(classes.sliderWrapper, classStyle)}>
      <Slider
        color="secondary"
        onChange={value ? onChange : (event, value) => handleInputChange(value)}
        ValueLabelComponent={ValueLabelComponent}
        value={value ? value : input.value}
        aria-labelledby={ariaLabelledBy ? ariaLabelledBy : 'input-slider'}
        min={min}
        step={ariaLabelledBy ? 1 : 0.1}
        max={max}
      />
    </div>
  );
};

export default CustomSliderField;
