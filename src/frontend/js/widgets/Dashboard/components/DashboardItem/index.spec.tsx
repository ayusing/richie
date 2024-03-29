import { render, screen } from '@testing-library/react';
import { DashboardSubItemsList } from './DashboardSubItemsList';
import { DashboardSubItem } from './DashboardSubItem';
import { DashboardItem, DEMO_IMAGE_URL } from '.';

describe('<DashboardItem />', () => {
  it('renders a DashboardItem in "full" mode', () => {
    render(
      <DashboardItem
        title="Become a React pro"
        code="Ref. 123"
        imageUrl={DEMO_IMAGE_URL}
        footer="Hi, i'm the footer"
      />,
    );

    expect(screen.getByText('Become a React pro')).toBeInTheDocument();
    expect(screen.getByText('Ref. 123')).toBeInTheDocument();
    expect(screen.getByText("Hi, i'm the footer")).toBeInTheDocument();
    expect(screen.getByTestId('dashboard-item__block__head__thumbnail')).toHaveAttribute(
      'src',
      DEMO_IMAGE_URL,
    );
  });

  it('renders a DashboardItem in "compact" mode', () => {
    render(
      <DashboardItem
        title="Become a React pro"
        code="Ref. 123"
        imageUrl={DEMO_IMAGE_URL}
        footer="Hi, i'm the footer"
        mode="compact"
      />,
    );

    expect(screen.getByText("Hi, i'm the footer")).toBeInTheDocument();

    expect(screen.queryByText('Become a React pro')).not.toBeInTheDocument();
    expect(screen.queryByText('Ref. 123')).not.toBeInTheDocument();
    expect(screen.queryByTestId('dashboard-item__block__head__thumbnail')).not.toBeInTheDocument();
  });

  it('renders a DashboardItem with children', () => {
    render(
      <DashboardItem title="Become a React pro" code="Ref. 123" imageUrl={DEMO_IMAGE_URL}>
        <DashboardSubItemsList
          subItems={[
            <DashboardSubItem title="Sub 1" />,
            <DashboardSubItem title="Sub 2" />,
            <DashboardSubItem title="Sub 3" />,
          ]}
        />
      </DashboardItem>,
    );

    screen.getByText('Sub 1');
    screen.getByText('Sub 2');
    screen.getByText('Sub 3');
  });
});
